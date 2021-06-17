from sklearn import svm,metrics
import pandas as pd

xor_data=[#P,Q,result
          [0,0,0],
          [0,1,1],
          [1,0,1],
          [1,1,0]
          ]

data=[]
label=[]
for row in xor_data:
    p=row[0]
    q=row[1]
    r=row[2]
    data.append([p,q])
    label.append(r)
    
clf=svm.SVC()
clf.fit(data,label)

pre=clf.predict(data)
print("예측결과:",pre)

ok=0;total=0
for idx,answer in enumerate(label):
    p=pre[idx]
    if p==answer:ok+=1
    total+=1
print("정답률:",ok,"/",total,"=",ok/total)

xor_df=pd.DataFrame(xor_data)
xor_data1=xor_df.loc[:,0:1]
xor_label=xor_df.loc[:,2]

clf=svm.SVC()
clf.fit(xor_data1,xor_label)
pre=clf.predict(xor_data1)

ac_score=metrics.accuracy_score(xor_label,pre)
print("정답률: ",ac_score)##git 연동 테스트 확인 자동


### sklearn.model_selection import train_test_split

### train_test_split(test_data,test_label)