
class CodeLoader:

	def Load(self,ruleName):

		try:

			fileObject = open(ruleName+"-args.py","r")
			source = fileObject.read()
			argument_schema = eval(source);

			fileObject = open(ruleName+"-rule.py","r")
			source = fileObject.read()

			arguments = {}
			for arg in argument_schema:
				if(argument_schema[arg] == 'int'):
					arguments[arg] = 10 #validate inputs and assign values


			print(arguments)
			result = eval(source,arguments,{})

			print("Code Loaded and Executed Successfully")
			print("Result = ",result)

		except Exception as loadError:
			print(str(loadError))





loader = CodeLoader()
loader.Load('test')






