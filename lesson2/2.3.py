#Nguyễn Mạnh Cường
import xml.dom.minidom
def main():
    #Sử dụng hàm parse() để đọc và phân tích file "sample.xml sau đó chuyển đổi nó thành biến đối tượng 'doc'.
    doc=xml.dom.minidom.parse(r"C:\Users\DELL\Documents\lesson1 Data science\Nguyen_Manh_Cuong_23174600007_DHKL17A1HN\lesson2\2.3.xml");

    #In ra In ra tên của node gốc và tag name của node đầu tiên trong file .xml
    print(doc.nodeName)
    print(doc.firstChild.tagName)
if __name__=="__main__":
    main();