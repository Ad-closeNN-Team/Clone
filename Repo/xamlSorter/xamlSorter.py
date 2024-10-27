import sys
import xml.etree.ElementTree as ET


def sort_xaml_file(input_file_path, output_file_path):
    try:
        # 注册命名空间
        ET.register_namespace('s', 'clr-namespace:System;assembly=mscorlib')
        ET.register_namespace('x', 'http://schemas.microsoft.com/winfx/2006/xaml')

        # 使用ElementTree加载XAML文件
        tree = ET.parse(input_file_path)
        root = tree.getroot()

        # 提取所有的s:String元素
        namespace = {'s': 'clr-namespace:System;assembly=mscorlib', 'x': 'http://schemas.microsoft.com/winfx/2006/xaml'}
        strings = root.findall('.//s:String', namespace)

        # 按照x:Key属性进行排序
        sorted_strings = sorted(strings, key=lambda x: x.attrib['{http://schemas.microsoft.com/winfx/2006/xaml}Key'])

        # 创建一个新的ResourceDictionary作为根元素
        new_root = ET.Element('ResourceDictionary', {
            'xmlns': "http://schemas.microsoft.com/winfx/2006/xaml/presentation",
            'xmlns:x': "http://schemas.microsoft.com/winfx/2006/xaml",
            'xmlns:s': "clr-namespace:System;assembly=mscorlib",
            'xml:space': "preserve"
        })

        # 将排序后的元素添加到新的根元素下
        for string in sorted_strings:
            new_root.append(string)

        # 创建新的ElementTree并写入到输出文件
        new_tree = ET.ElementTree(new_root)
        new_tree.write(output_file_path, encoding='unicode', xml_declaration=True)

        print("File sorted and saved successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python xamlSorter.py <input_file_path> <output_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    sort_xaml_file(input_file_path, output_file_path)
