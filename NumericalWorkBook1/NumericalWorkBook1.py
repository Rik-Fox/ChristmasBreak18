n = 80
a = zeros(Float32,n)

a[1]=1
a[2]=2/3

for i=3:80
    a[i] = 2*a[i-1] - (8/9)*a[i-2]
end

# plot(a,label=\"Float32\")
# title!(\"First 80 Terms of given Recursive Function\")
# yaxis!(\"Value of function\",:log10)
# xaxis!(\"Term Index\")"

n = 80\
b = zeros(Float64,n)

b[1]=1
b[2]=2/3

for i=3:80
    b[i] = 2*b[i-1] - (8/9)*b[i-2]
end

# plot(a,label=\"Float32\")\n",
# plot!(b,label=\"Float64\")\n",
# title!(\"First 80 Terms of given Recursive Function\")\n",
# yaxis!(\"Value of function\",:log10)\n",
# xaxis!(\"Term Index\")"

function perturb(p,n)

    s = zeros(n)

    for i=1:n

    s[i] = (1-(3/2)*p)*(2/3)^(i-1) + (3/2)*p*(4/3)^(i-1)  #perturbed solution
    end

    return s
end

n=128

             #ϵ's of varying magnitude to show perturbation growth\n",
ϵ_1 = 1E-8   # ~Float32\n",
ϵ_2 = 1E-16  # ~Float64\n",
ϵ_3 = 1E-32  # ~BigFloat\n",
                #arrays holding the analytical solution solved with the varying ϵ values\n",
e_1=perturb(ϵ_1,n)
e_2=perturb(ϵ_2,n)
e_3=perturb(ϵ_3,n)

# plot(e_1,label=\"ϵ ~Float32\")\n",
# plot!(e_2,label=\"ϵ ~Float64\")\n",
# plot!(e_3,label=\"ϵ ~BigFloat\")\n",
# title!(\"Exact solution after including error term\")\n",
# yaxis!(\"Value of function\",:log10)\n",
# xaxis!(\"Term Index\")"

n = 80
c =zeros(BigFloat,n)

c[1]=BigFloat(1)
c[2]=BigFloat(2)/BigFloat(3)

for i=3:80
    c[i] = BigFloat(2)*(c[i-1]) - BigFloat(8)/BigFloat(9)*(c[i-2])
end
m = 50

    # "plot(a,label=\"Float32\")\n",
    # "plot!(b,label=\"Float64\")\n",
    # "plot!(c,label=\"BigFloat\")\n",
    # "title!(\"First 80 terms of Given Recursive Function\")\n",
    # "yaxis!(\"Value of function\",:log10)\n",
    # "xaxis!(\"Term Index\")"

function mergepresorted(A::Array{Int64,1}, B::Array{Int64,1})
    if length(A) == 0
        return B
    elseif length(B) == 0
        return A
    elseif A[1] < B[1]
        return vcat([A[1]], mergepresorted(A[2:end], B))
    else
        return vcat([B[1]], mergepresorted(A, B[2:end]))
    end
end"


C=Array(1:2:99)
D=Array(2:2:100)

E = mergepresorted(C,D)

# plot(C,label=\"1st pre-sorted Array\")\n",
#     "plot!(D,label=\"2nd pre-sorted Array\")\n",
#     "plot!(E,label=\"Merged Arrays\")\n",
#     "title!(\"Merge presorted Algorithm Check\")\n",
#     "yaxis!(\"Value of Array Element\")\n",
#     "xaxis!(\"Array Index\")"

    function mergesort(A,B,n)
    if n == 1
       C= mergepresorted(A,B)
       return C
   elsen,
        m = Int64(n/2)

       C= mergepresorted(mergesort(A[1:m],A[m+1:n],m),mergesort(B[1:m],B[m+1:n],m))
        return C
    end
end



m = 6
n = Int64(2^m)

A = rand(1:100,n)
B = rand(1:100,n)
X = 1:1:2*n

C = mergesort(A,B,n)

    # "scatter(X,A,label=\"1st Array of Random Integers\",size=(800,400))\n",
    # "scatter!(X,B,label=\"2nd Array of Random Integers\",size=(800,400))\n",
    # "scatter!(X,C,label=\"Sorted Array\")\n",
    # "title!(\"Recursive Implementation of a MergeSort algorithm\")\n",
    # "yaxis!(\"Value of Array Element\")\n",
    # "xaxis!(\"Array Index\")"



#have only set to 13 as takes while for anything more\n",

k =13

runtimes =zeros(k)
th =zeros(k)
number = zeros(k)
for i=1:k

    m = i
    n = Int64(2^m)

    A = rand(1:100,n)
    B = rand(1:100,n)

    C =  @timed mergesort(A,B,n)

    runtimes[i] = C[2]
    th[i]       = n*log(n)
    number[i]=n
end

#    "plot(number,runtimes,marker=4,label=\"Empirical Times\",size=(800,400))\n",
