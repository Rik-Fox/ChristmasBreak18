def GRWalk(n,M,mu,sigma):

    X = np.array(np.random.normal(mu,sigma,size=(n,M)))

    Y = np.zeros(shape=(n,M))
    Y[:,0] = 0

    for j in range(0,M):
        Y[:,j] = np.cumsum(X[:,j])

    return Y
