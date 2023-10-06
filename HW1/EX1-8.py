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
    
    # Create a set of unique element names
    element_names = set()
    for connection in netlist:
        element_names.add(connection[0])
        element_names.add(connection[1])
    
    element_names = sorted(list(element_names))
    
    # Create a mapping from element names to integers
    element_to_int = {element: idx for idx, element in enumerate(element_names)}
    
    # Initialize the connectivity matrix with zeros
    matrix_size = len(element_names)
    connectivity_matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
    
    # Fill in the connectivity matrix based on the netlist
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

# %%
if __name__ == "__main__":
    netlist_file = "C:\\Users\\Jinge\\Programming\\Python\\BUAA-EDA-Homework\HW1\\netlist.2"
    output_file = "cmat.txt"
    
    element_names, connectivity_matrix = generate_connectivity_matrix(netlist_file)
    # write_connectivity_matrix_to_file(element_names, connectivity_matrix, output_file)
    
    print("Connectivity matrix has been written to 'cmat.txt'.")

# %%



