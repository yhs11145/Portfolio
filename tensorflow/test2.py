import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() 

I=tf.placeholder(tf.float32,[2,4])
i=[[1,2,3,4],[5,6,7,8]]
W=tf.placeholder(tf.float32,[4,2])
w=[[1,1],[2,2],[3,3],[4,4]]

node=tf.matmul(I,W)

sess=tf.Session()
sess.run(tf.global_variables_initializer())

print(sess.run(node,feed_dict={I:i,W:w}))

sess.close()

''' ##그래프 생성
x=tf.constant(10)
y=tf.constant(5)
c=tf.add(x,y)

sess=tf.Session()
print(sess.run(c))
sess.close()
'''
''' ## 실행시키기
a=tf.constant('1')

print(a)
'''

'''
a = tf.placeholder('float')
b = tf.placeholder('float')

y = tf.multiply(a, b)

sess = tf.Session()

print(sess.run(y, feed_dict={a:3, b:3}))
'''