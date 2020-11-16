function x = nagauss1(a,b,flag)
%用途 顺序高斯消去法解线性方程ax=b
%a 系数矩阵 b 右端列向量
%flag 若为0，则显示中间过程 否则不显示默认值为0
%x：解向量
if nargin<3,flag=0;end
n=length(b);a=[a,b];
%消元
for k=1:(n-1)
    a((k+1):n,(k+1):(n+1)) = a((k+1):n,(k+1):(n+1))...
        -a((k+1):n,k)/a(k,k)*a(k,(k+1):(n+1));
    a((k+1):n,k) = zeros(n-k,1);
    if flag==0,a,end
end
%回代
x=zeros(n,1);
x(n)=a(n,n+1)/a(n,n);
for k=n-1:-1:1
    x(k) = (a(k,n+1)-a(k,(k+1):n)*x((k+1):n))/a(k,k);
end