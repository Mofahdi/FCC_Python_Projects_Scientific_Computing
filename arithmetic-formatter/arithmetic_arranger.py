def arithmetic_arranger(problems, show_results=False):
	if len(problems)>5:
		return 'Error: Too many problems.'
	
	arranged_problems=str()
	line1=str(); line2=str(); line3=str(); line4=str()
	for i, problem in enumerate(problems):
		prob_split=problem.split();  
		operation=prob_split[1]; 
		if operation!='+' and operation != '-':
			return "Error: Operator must be '+' or '-'."
		
		first=prob_split[0]; second=prob_split[2]
		if not first.isdigit() or not second.isdigit():
			return "Error: Numbers must only contain digits."
		
		if len(first)>4 or len(second)>4:
			return "Error: Numbers cannot be more than four digits."
			
		space=max(len(prob_split[0]), len(prob_split[2]))
		result=str(int(prob_split[0])+int(prob_split[2])) if operation=='+' else str(int(prob_split[0])-int(prob_split[2]))
		line1+=first.rjust(space+2)+"".center(4) if i!=len(problems)-1 else first.rjust(space+2)
		line2+=operation+" "+second.rjust(space)+"".center(4) if i!=len(problems)-1 else operation+" "+second.rjust(space)
		line3+="".center(space+2, '-')+"".center(4) if i!=len(problems)-1 else "".center(space+2, '-')
		line4+=result.rjust(space+2)+"".center(4) if i!=len(problems)-1 else result.rjust(space+2)
	
	if show_results:
		arranged_problems+=line1+'\n'+line2+'\n'+line3+'\n'+line4
	else:
		arranged_problems+=line1+'\n'+line2+'\n'+line3
		
	return arranged_problems
