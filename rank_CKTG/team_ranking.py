from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import re
import psycopg2

driver = webdriver.Chrome()
driver.get('https://lolesports.com/vi-VN')  # Link của trang web
sleep(5)  

acpt = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/button[2]")
acpt.click()
sleep(2)

power_ranking = driver.find_element(By.LINK_TEXT, "POWER RANKINGS")
power_ranking.click()
sleep(3)

data = []
def collect_data():
    for i in range(1, 80+1):
        teams = driver.find_elements(By.XPATH, f"/html/body/main/div[2]/div/div[2]/div[1]/div/div[2]/table/tbody/tr[{i}]")
        for team in teams:
            clean_text = team.text.strip().replace('\n', ' ').replace('\t', ' ')  
            data.append(clean_text)

collect_data()
driver.quit()


def process_data(data):
    processed_data = []
    pattern = re.compile(
        r"(\d+)\s+-\s+([A-Za-z0-9\.\'!\s]+)\s+([A-Z]+)\s+(\d+)\s+đ\s+([\d\-]+)"
    )
    
    for row in data:
        match = pattern.match(row)
        if match:
            rk = match.group(1)  # Rank
            name = match.group(2).strip()  # Tên đội
            area = match.group(3).strip()  # Khu vực
            pts = match.group(4)  # Điểm số
            w_l = match.group(5)  # Thắng - Thua
            processed_data.append((rk, name, area, pts, w_l))
    
    return processed_data

processed_data = process_data(data)

def create_table():
    conn = psycopg2.connect(
        host="localhost",
        port="5433",
        database="world_ranking",
        user="postgres",
        password="44444"
    )
    cur = conn.cursor()
   
    cur.execute("""
        CREATE TABLE IF NOT EXISTS team_ranking (
            rk INT PRIMARY KEY,
            name VARCHAR(255),
            area VARCHAR(100),
            pts INT,
            w_l VARCHAR(50)
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()

def insert_data(processed_data):
    conn = psycopg2.connect(
        host="localhost",
        port="5433",
        database="world_ranking",
        user="postgres",
        password="44444"
    )
    cur = conn.cursor()

   
    insert_query = """
        INSERT INTO team_ranking (rk, name, area, pts, w_l)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (rk) DO NOTHING;  
    """

    cur.executemany(insert_query, processed_data)

    conn.commit()
    cur.close()
    conn.close()

create_table()
insert_data(processed_data)
