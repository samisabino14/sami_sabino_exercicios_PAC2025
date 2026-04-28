import re, time, os, json, requests
from urllib.parse import urlparse

rules = [
    r'^(disallow|allow):\s*(.+)$',
    r'^(https?:\/\/[^\/]+)',
    r'(?:href|src|action)\s*=\s*["\'](?![^"\']*(?:\.css(?:\?|$)|/css/))([^"\']+)["\']', # Compila diferentes padrões de links
    r'^User-agent:\s*\*\s*((?:\n(?!User-agent:).*)*)',
    
]

visited = set()


def main():
    try:
        pages_to_visit = read_file("sites.json", "json")

        make_to_visit(pages_to_visit)
        
        print(visited)
            
    except Exception as e:
        print(e)
        
def get_site_title(html_page):
    return re.search("<title>(.*?)</title>", html_page, re.IGNORECASE)

def get_path(url):
    return urlparse(url).path
    
def is_blocked(url, disallow_list):
    path = get_path(url)
    
    for rule in disallow_list:
        # remover wildcard simples
        clean_rule = rule.replace("*", "")
        
        if path.startswith(clean_rule):
            return True
        
    return False

def send_request(url, method='get', data=None):
    """_summary_

    Args:
        url (str): url na qual se pretende fazer a requisição.
        method (str, optional): o verbo da requisição, usa get como padrão. Defaults to 'get'.
        data ({}): o corpo da requisição (caso haja a necessidade), usa None como padrão.
    Returns:
        response: response
    """
    headers = {
        "User-Agent": "Uso académico e formativo"
    }
    
    return requests.request(method.lower(), url, headers=headers, data=data)

def read_robots_content(baseUrl):
    # Garantir que não termine com /
    baseUrl = baseUrl.rstrip('/')
    robotsUrl = f"{baseUrl}/robots.txt"
    response = send_request(robotsUrl)
    
    # 3) Verificar se contém HTML
    if "<html" in response.text.lower() or "<!doctype" in response.text.lower():
        # PODE EXPLORAR OS LINKS NO DOC HTML
        return None
    
    return response.text

def read_robots_lines(robot_txt):
    return [line.strip() for line in robot_txt.splitlines() if line.strip()]


def get_standard(rule_position):
    return re.compile(
        rules[rule_position],
        re.IGNORECASE | re.MULTILINE
    )

def extract_disallow_routes_in_robots(content):
    if not content:
        return []

    content = content.replace("\r\n", "\n").replace("\r", "\n")
    lines = content.split("\n")

    routes = []
    block_inside = False

    for line in lines:
        line = line.strip()

        if line.lower().startswith("user-agent: *"):
            block_inside = True
            continue

        if block_inside and line.lower().startswith("user-agent:"):
            break

        if block_inside:
            if line.lower().startswith("disallow:") or line.lower().startswith("allow:"):
                parts = line.split(":", 1)
                if len(parts) < 2:
                    continue
                route = parts[1].strip()
                if not route:
                    continue
                routes.append(route)

    return routes

def extract_rule(line):
    standard = get_standard(0)
    
    match = standard.search(line)

    return match[2] if match else None

def get_base_url(url):
    standard = get_standard(1)

    match = standard.search(url)

    return match[1] if match else None

def make_to_visit(pages_to_visit):
    
    for page in pages_to_visit:
        
        if page["link"]:
            
            baseUrl = get_base_url(page["link"])
            
            robot_content = read_robots_content(baseUrl)
            
            disallow_list = extract_disallow_routes_in_robots(robot_content)
            
            is_restrict = is_blocked(page["link"], disallow_list)
            
            if is_restrict is True: # "Explorar este link..."
                print(f"\n{'*' * 80}\n\nA página {page["link"]} não pode ser explorada. \n\t* Está protegida por robots.txt!\n\n{'*' * 80}\n")
                continue
            else:
                crawler_response = crawler(page["link"])
                links, title = extract_tile_and_links(crawler_response)
                
                reuslt = {
                    "url": page["link"],
                    "titulo": title,
                    "links": links
                }

                print(reuslt)

                """ 
                for link in links:
                    complete_link = baseUrl + link if link.startswith("/") else link
                """
                    
        else:
            print(f"\nLink vazio: {page["title"]}")  
            
        delay_1s() # Cria um delay de 1s para cada página visitada
        

def crawler(url):
    
    if url in visited:
        return
    
    visited.add(url)
    
    response = send_request(url)
    
    return response.text

def extract_tile_and_links(html_page):
    """Esta função serve para extrair todos os links em uma página HTML.

    Args:
        html_page (string): página na qual se pretende encontrar e extrair links.

    Returns:
        list[string]: retorna uma lista de strings (links).
    """
    standard = get_standard(2)
    
    links = standard.findall(html_page)
    title = get_site_title(html_page)
    
    return links, title[1]

def read_abs_path(filename):
    # Caminho absoluto da raíz do projeto
    root = os.path.dirname(os.path.abspath(__file__))
        
    return os.path.join(root, filename) 

def read_file(filename, type_file):
    # Caminho absoluto da raíz do projeto
    path = read_abs_path(filename)
    
    if not os.path.exists(path): # Verifica a existência do ficheiro no caminho passado
        raise FileNotFoundError(f"Ficheiro não encontrado: {path}")
    
    with open(path, "r", encoding='utf-8') as file:
        return json.load(file) if type_file == 'json' else file.read() # Verifica qual o tipo pretendido e retorna json ou outro tipo qualquer
    
def delay_1s():
    time.sleep(1)