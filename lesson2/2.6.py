import requests
import xml.etree.ElementTree as ET
import csv

def download_rss(url, file_name):
    response = requests.get(url)
    
    with open(file_name,'wb') as file:
        file.write(response.content)

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    news_list = []

    for item in root.findall('.//item'):
        news_item = {}
        for child in item:
            if child.tag == 'title':
                news_item['title'] = child.text
            elif child.tag == 'link':
                news_item['link'] = child.text
            elif child.tag == 'description':
                news_item['description'] = child.text
            # Thêm các trường khác nếu cần

        news_list.append(news_item)

    return news_list

def save_to_csv(news_list, csv_file):
    fieldnames = ['title', 'link', 'description'] 

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for news_item in news_list:
            writer.writerow(news_item)

if __name__ == "__main__":
    rss_url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
    xml_file_name = "rss_feed.xml"
    csv_file_name = "news.csv"

    # Tải RSS feed
    download_rss(rss_url, xml_file_name)

    # Phân tích cú pháp XML
    news_list = parse_xml(xml_file_name)

    # Lưu vào tệp CSV
    save_to_csv(news_list, csv_file_name)
