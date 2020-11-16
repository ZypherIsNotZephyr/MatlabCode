function a=nalupad(a)
n = length(a);
a(2:n,1)=a(2:n,1)/a(1,1);
for k=2:n
    a(k,k:n)=a(k,k:n)-a(k,1:k-1)*a(1:k-1,k:n);
    a(k+1:n,k)=(a(k+1:n,k)-a(k+1:n,1:k-1)*a(1:k-1,k))/a(k,k);
end