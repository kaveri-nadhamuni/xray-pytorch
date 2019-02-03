f8k_train_caps=open("f8k_train_caps.txt","r")
f8k_test_caps=open("f8k_test_caps.txt","r")
f8k_dev_caps=open("f8k_dev_caps.txt","r")

num_lines=0
for line in f8k_train_caps:
        
        num_lines += 1
print("train caption size",num_lines)  


num_lines=0
for line in f8k_test_caps:
        
        num_lines += 1
print("test caption size",num_lines) 

num_lines=0
for line in f8k_dev_caps:
        
        num_lines += 1
print("dev caption size",num_lines) 