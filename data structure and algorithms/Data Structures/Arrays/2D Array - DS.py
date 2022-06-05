# add sum of all required elements and take max    
  
  
  
  mx=-999999999
    sum=0
    for i in range(4):
        for j in range(4):
            sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            mx=max(sum,mx)
    return mx
