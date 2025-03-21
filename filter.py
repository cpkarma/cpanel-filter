import sys
import subprocess

def install_modules():
    modules = ['tqdm', 'colorama']
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            print(f"Installing {module}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])

install_modules()

import re
from tqdm import tqdm
from colorama import init, Fore, Style

init()

def x_y():
    a_b = """
    =============================================
                cPanel List Filter
    =============================================
            Powered by: Karma Syndicate
    =============================================
    """
    print(f"{Fore.MAGENTA}{a_b}{Style.RESET_ALL}")

def y_z(c_d):
    c_d = ''.join(c_d.split())
    
    if not c_d:
        return None
    
    c_d = c_d.replace('/:', ':')
    
    if not c_d.startswith('http'):
        c_d = 'https://' + c_d
    
    c_d = c_d.replace('http://', 'https://')
    
    e_f = [
        'https://-',
        'https://--',
        'https://---',
        'https://.',
        'https://..'
    ]
    for f_g in e_f:
        c_d = c_d.replace(f_g, 'https://')
    
    c_d = c_d.replace(':2082', ':2083')
    
    if ':2083:' in c_d:
        g_h = c_d.split(':2083:')
        if len(g_h) == 2:
            h_i = g_h[1].split(':')
            if len(h_i) == 2:
                c_d = f"{g_h[0]}:2083|{h_i[0]}|{h_i[1]}"
    
    c_d = c_d.replace('/|', '|')
    
    return c_d

j_k = re.compile(r'^https://[a-zA-Z0-9.-]+:2083\|[^|]+\|[^|]+$')

x_y()

k_l = set()

print(f"{Fore.CYAN}Please enter the name of the input file (e.g., list.txt): {Style.RESET_ALL}", end='')
m_n = input()

try:
    with open(m_n, 'r', encoding='utf-8') as n_o:
        o_p = sum(1 for p_q in n_o)
    
    with open(m_n, 'r', encoding='utf-8') as n_o:
        for q_r in tqdm(n_o, total=o_p, desc=f"{Fore.YELLOW}Processing lines{Style.RESET_ALL}",
                        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
            r_s = y_z(q_r)
            if r_s:
                k_l.add(r_s)

    s_t = {u_v for u_v in k_l if j_k.match(u_v)}
    
    with open('filtered_list.txt', 'w', encoding='utf-8') as v_w:
        for w_x in tqdm(sorted(s_t), desc=f"{Fore.GREEN}Writing output{Style.RESET_ALL}",
                        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
            v_w.write(w_x + '\n')
            
    print(f"\n{Fore.GREEN}Processing complete! Results saved to filtered_list.txt{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Original lines processed, {len(s_t)} valid lines saved{Style.RESET_ALL}")

except UnicodeDecodeError:
    print(f"{Fore.RED}UTF-8 decoding failed, trying latin-1 encoding...{Style.RESET_ALL}")
    k_l.clear()
    try:
        with open(m_n, 'r', encoding='latin-1') as n_o:
            o_p = sum(1 for p_q in n_o)
            
        with open(m_n, 'r', encoding='latin-1') as n_o:
            for q_r in tqdm(n_o, total=o_p, desc=f"{Fore.YELLOW}Processing lines{Style.RESET_ALL}",
                            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
                r_s = y_z(q_r)
                if r_s:
                    k_l.add(r_s)
                    
        s_t = {u_v for u_v in k_l if j_k.match(u_v)}
        
        with open('filtered_list.txt', 'w', encoding='utf-8') as v_w:
            for w_x in tqdm(sorted(s_t), desc=f"{Fore.GREEN}Writing output{Style.RESET_ALL}",
                            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
                v_w.write(w_x + '\n')
                
        print(f"\n{Fore.GREEN}Processing complete with latin-1! Results saved to filtered_list.txt{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Original lines processed, {len(s_t)} valid lines saved{Style.RESET_ALL}")
        
    except Exception as x_y:
        print(f"{Fore.RED}Failed with both encodings: {str(x_y)}{Style.RESET_ALL}")
except FileNotFoundError:
    print(f"{Fore.RED}Error: {m_n} not found in the current directory{Style.RESET_ALL}")
except Exception as x_y:
    print(f"{Fore.RED}An error occurred: {str(x_y)}{Style.RESET_ALL}")