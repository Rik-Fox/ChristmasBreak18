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
