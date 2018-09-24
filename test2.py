import tensorflow as tf 

matrix1=tf.constant([[3,3]])
matrix2=tf.constant([[2],[2]])

protduct=tf.matmul(matrix1,matrix2)     #矩阵乘法


#形式一
sess=tf.Session()
result=sess.run(protduct)
print(result)
sess.close()

