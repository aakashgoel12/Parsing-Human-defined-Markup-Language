# Program to parse the HML (Human defined Markup Language)... 
import re

# i/p: ip_list of hml tags, o/p is dictionary storing tag & information of it.
def parse_hml(ip_list):
	# storing Tag names & will be popped out as we encounter end of tag..
	tag_list=[]
	# Dictionary storing all the tag info and tag names in defined format..
	dictionary_tag_info={}
	# regex to find opening of Tags
	reg_open_tag= r"<"+re.escape("tag")+r"\d+"
	# regex to find closing of Tags
	reg_close_tag = r"</"+re.escape("tag")+r"\d+"
	# regex to find data ( values) going to be stored in dictionary_tag_info
	reg_dict_data=r"<"+re.escape("tag")+r"\d+\ +"+r"([a-zA-Z=\ ]+)*"+r">"
	for i in ip_list:
			if(re.search(reg_open_tag,i)):
				tag_list.append(re.search(reg_open_tag,i).group().strip('<'))
				dictionary_tag_info['.'.join(tag_list)]={}
				if(re.search(reg_dict_data,i)):
					dict_data=re.search(reg_dict_data,i).groups()[0]
					key_value_list=re.split(r"\W+",dict_data)
					for j in range(0,len(key_value_list),2):
						if(j+1<len(key_value_list)):
							dictionary_tag_info['.'.join(tag_list)][key_value_list[j]]=key_value_list[j+1]
						else:
							dictionary_tag_info['.'.join(tag_list)][key_value_list[j]]=''
			elif(re.search(reg_close_tag,i)):
				tag_list.remove(re.search(reg_close_tag,i).group().strip('</'))
	return dictionary_tag_info

# Processing of Answering the User Query defined in tag.txt file
def process_query(ip_no,op_no,data,dictionary_tag_info):
	for i in range(1+ip_no,1+ip_no+op_no):
		op=data[i]
		op=op.strip('\r\n')
		key_value=op.split('~')
		key=op.split('~')[0]
		value=op.split('~')[1]
		# print key
		# print value
		if(dictionary_tag_info.has_key(key)):
			if(dictionary_tag_info[key].has_key(value)):
				print dictionary_tag_info[key][value]
			else:
				print "Not Found!"
		else:
			print "Not Found!"

if __name__ == '__main__':
	#opening file containing Human defined tags ..
	data=open('tag.txt','r').readlines()
	temp_data= data[0].strip('\r\n').split()
	ip_no=int(temp_data[0])
	op_no=int(temp_data[1])
	ip=''
	# List containing HML
	ip_list = map(lambda x:x.replace("\"",'').strip('\r\n'), data[1:ip_no+1])
	# processing
	# calling of function --  Parsing of HML 
	dictionary_tag_info=parse_hml(ip_list)
	# calling of function -- Processing of Answering the User Query defined in tag.txt file
	process_query(ip_no,op_no,data,dictionary_tag_info)