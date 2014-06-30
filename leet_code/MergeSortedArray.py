import copy

class Solution:
	# @param A  a list of integers
	# @param m  an integer, length of A
	# @param B  a list of integers
	# @param n  an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		c = range(m+n)
		i=0
		j=0
		k=0
		print 'm:',m
		print 'n:',n
		while i<m or j<n:
			print 'i:',i
			if i==m:
				c[k]=B[j]
				j=j+1
			elif j==n:
				c[k]=A[i]
				i=i+1
			elif A[i]>B[j]:
				c[k]=B[j]
				j=j+1
			else: 
				c[k]=A[i]
				i=i+1
			print 'k:',k
			k=k+1		
		
		for a in A:
			A.remove(a)
		
		print "c:",c
			
		for cc in c:
			A.append(cc)
			
		#A=copy.copy(c)
		#for 
		#A.append(1)
		print "A:",A

if __name__ == '__main__':
	s = Solution()
	A=[1]
	B=[2]
	s.merge(A,len(A),B,len(B))
	print "A:",A