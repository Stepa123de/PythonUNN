MyDict = {
"какая версия языка сейчас актуальна?" : "python3",
"какая кодировка используется в строках?" : "utf8",
"какой оператор сравнения нужно использовать для работы с None и bool?" : "is",
"сколько значений есть у bool?" : "2"}

TrAnswers = 0;

for i in MyDict:
	print(i);
	S = input();
	if MyDict[i] == S.lower():
		print("Ответ {} верен.".format(S));
		TrAnswers += 1;
	else:
		print("Неверный ответ.");

print("All Answers {} / True Answers {}".format(len(MyDict),TrAnswers));