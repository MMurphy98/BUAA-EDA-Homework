# %% [markdown]
# 该编程题目要求cmat为对角矩阵，且对角线上的元素为0。编程由python语言完成，需要Jupyter Notebook 和 numpy，代码如下：

# %%
# 定义检测矩阵连接性函数
def check_connectivity_matrix(matrix):
    n = len(matrix)
    errors_found = False

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                print(f"错误的元素在 {i + 1} 和 {j + 1} 之间；")
                errors_found = True
            if i == j and matrix[i][j] != 0:
                print(f"元素 {i + 1} 自身错误；")
                errors_found = True

    if not errors_found:
        print("矩阵的连接性正确！")


# %%
# 生成对角阵cmat并验证

import numpy as np

# 定义矩阵的大小
matrix_size = 100

# 生成100以内的随机整数矩阵
cmat = np.random.randint(1, 100, size=(matrix_size, matrix_size))

# 通过与转置求和得到对称阵
cmat = (cmat + cmat.T) // 2

# 将对角线元素设置为0
np.fill_diagonal(cmat, 0)



# %%
check_connectivity_matrix(cmat)

# %%
cmat_error = cmat
# 随机修改两个元素之间的距离，对应的check_connectivity_matrix会发现4个错误
for i in range(2):
    index_i = np.random.randint(0,matrix_size-1)
    index_j = np.random.randint(0,matrix_size-1)
    random_value = np.random.randint(1, 100)
    print(f"修改cmat[{index_i+1},{index_j+1}] = {random_value}")
    cmat_error[index_i][index_j] = random_value

check_connectivity_matrix(cmat_error)


