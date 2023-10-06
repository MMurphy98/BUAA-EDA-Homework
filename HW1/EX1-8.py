# %%
# 从 "netlist.2"中读取文件，并转化为matrix
def generate_connectivity_matrix(netlist_file):
    netlist = []
    
    # 打开文件以 ','分割，获得所有的节点，并删除两侧空格和括号
    with open(netlist_file, 'r') as file:
        for line in file:
            line = line.strip()
            line = line.strip(")")
            line = line.strip("(")
            if line:
                elements = line.split(',')
                netlist.append((elements[0].strip(), elements[1].strip()))
    
    # 使用set记录节点名称，保证不会重复
    element_names = set()
    for connection in netlist:
        element_names.add(connection[0])
        element_names.add(connection[1])

    # 对节点名称进行重排
    element_names = sorted(list(element_names))
    
    # 枚举所有节点并将其映射到数字上，并用节点名获得其数字（字典）
    element_to_int = {}
    for idx, element in enumerate(element_names):
        element_to_int.update({element: idx})

    # 创建空矩阵
    matrix_size = len(element_names)
    connectivity_matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

    # 遍历所有网表
    for connection in netlist:
        i = element_to_int[connection[0]]
        j = element_to_int[connection[1]]
        connectivity_matrix[i][j] += 1
        connectivity_matrix[j][i] += 1
    
    return element_names, connectivity_matrix

# %%
# 将 matrix 写入cmat文件
def write_connectivity_matrix_to_file(element_names, connectivity_matrix, output_file):
    with open(output_file, 'w') as file:
        # 第一行为所有节点名
        file.write(','.join(element_names) + '\n')
        for row in connectivity_matrix:
            file.write(','.join(map(str, row)) + '\n')

# %% [markdown]
# 

# %%
if __name__ == "__main__":
    netlist_file = "netlist.2"
    output_file = "cmat.csv"
    element_names, connectivity_matrix = generate_connectivity_matrix(netlist_file)
    write_connectivity_matrix_to_file(element_names, connectivity_matrix, output_file)
    
    print("正常成为cmat.csv文件")


