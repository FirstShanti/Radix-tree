class Node:

	def __init__(self):
		self.children = {}
		self.parent = {}
		self.endOfWord = False

	def insert_code(self, word):
		'''
		Loop through characters in a word and keep adding them at a new node, linking them together
		If char already in node, pass
		Increment the current to the child with the character
		After the characters in word are over, mark current as EOW
		'''
		for char in word:
			if char in self.children.keys():
				pass
			else:
				self.children[char] = Node()
			self = self.children[char]
		self.endOfWord = True

	def all_codes(self, node=None, prefix='', results=[]):
		'''
		Recursively call the loop
		Prefix will be prefix + current character
		Node will be position of char's child
		results are passed by reference to keep storing result

		Eventually, when we reach EOW, the prefix will have all the chars from starting and will be the word that we need. We add this word to the result
		'''
		if not node:
			node = self
		if node.endOfWord:
			results.append(prefix)
		for char in node.children.keys():
			results = self.all_codes(node=node.children[char], prefix=prefix + char, results=results)
		return results

	def search_code(self, word):
		'''
		Loop through chars of the word in the trie
		If char in word is not in trie.children(), return
		If char found, keep iterating
		After iteration for word is done, we should be at the end of word. If not, then word doesn't exist and we return false.
		'''
		search_result = True
		for char in word:
			if char in self.children.keys():
				pass
			else:
				search_result = False
				break
			self = self.children[char]
		if not self.endOfWord:
			search_result = False
		return search_result

	def parents(self, word):
		'''
		Find parent word of this current word
		We loop through characters in the word along the trie
		If find knots with endOfWord and this size not bigger than word, append its in result
		'''
		results = []
		for char in word:
			if char in self.children.keys():
				pass
			else:
				break
			self = self.children[char]
			if self.endOfWord and word.index(char) < len(word) - 1:
				results.append(word[0:word.index(char)+1:])
		return results

	def childrens(self, prefix, results):
		'''
		We loop through charcters in the prefix along with trie
		If mismatch, return
		If no mismatch during iteration, we have reached the end of prefix. Now we need to get words from current to end with the previx that we passed. So call all_codes with prefix
		'''
		for char in prefix:
			if char in self.children.keys():
				pass
			else:
				return
			self = self.children[char]
		self.all_codes(self, prefix=prefix, results=results)
