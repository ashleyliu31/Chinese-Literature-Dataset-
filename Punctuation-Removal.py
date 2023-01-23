import re, string, os

#this is the list of punctuations to be removed
punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'

target_dir = r"[enter local directory here]"

print(re.sub(r"[%s]+" % punc, "", text))

f_in = open('filename.txt', 'rt', encoding="utf8")

#this loop removes punctuations in the file by replacing all punctuations listed above with nothing

f_out = open(os.path.join(target_dir, f_in.replace('.txt', '.txt')), 'w+')
for line in f_in:
    f_out.write(re.sub(r"[%s]+" % punc, "", line))





