def ddiff_tab(x, y):
    #This function will create a number of sets which represent each row 
    #of the difference coefficients in tabular form
    #using the sets of points x and y.
	N=len(x)
    #This will act as the stopping criteria for the number of coefficients
	dd = [ [0. for j in range(N+1)] for i in range(N)]
    #This forms a blank array of sets to be filled in for the illustration.
	for i in range(N):
        #here we fill in the known xi and respective yi values into the array
		dd[i][0]=x[i]
		dd[i][1]=y[i]

	for j in range(2,N+1):
		for i in range(N-j+1):
            #we then calculate the remaining coefficients
			df = dd[i+1][j-1] - dd[i][j-1]
			dx = dd[i+j-1][0] - dd[i][0]
            #and then add them into their positions into the tabular array
			dd[i][j]= df/dx
	return dd;

def pr(i, xp, x):
    #we will use this function to calculate the value of
    #p = (x-x[0])*(x-x[1])*...*(x-x[n-1])
    #for each coefficient in the tabular array that varies with i.
	p = 1.
	for l in range(i):
        #here i will be the number of x values and hence the number of 
        #coefficients in the divided difference formula.
		p = p * (xp - x[l])
	return p;


def print_dd(dd):
    #This function will take the arragement of sets from the ddiff_tab 
    #function and arrage them into tabular form to be better illustrated.
	N=len(dd[0])-1
    #Here N is the stopping criteria as it represents the number of columns -1.
	for i in range(N):
		for j in range(N+1):
			print(round(dd[i][j], 4), "\t", end = " ");
            #this allocates each coefficient to its respective column[i]
            #and row[j].
		print("");

def poly_dd(xp,x,y):
    #xp- the value the polynomial will be evaluated at.
    #x,y - The sets of x and y values.
    #poly - the value of the polynomial evaluated at xp.
    #dd - array of each coefficient of the divided difference formula
    #The number of terms the polynomial will have is determined as len(x)-1
    #as i stops at this point. 
    dd = ddiff_tab(x,y)
    poly=0
    for i in range(len(x)):
        #the function then evaluates each term in the polynomial and
        #adds it to the previous term until all terms have been summed.
        poly = pr(i,xp,x)*dd[0][i+1] + poly
    print(f'The value of the polynomial at {xp} is {poly}')
    
x=[2,6,5,8]
y=[9.5,9,18.5,14]
poly_dd(2,x,y)
