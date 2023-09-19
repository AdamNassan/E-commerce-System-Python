#!/bin/bash
 clear  # Clear the terminal screen
while true ; do 
   read -p "Is the dictionary.txt file exist or not? " dicChoice
   if [[ "$dicChoice" == "yes" ]]; then 	#If the file exist (user choose yes) 
      while true; do
        read -p "Enter the path of the file: " dicFile 	#ask for it's path
        if [ -e "$dicFile" ]; then 	#Check if the file exist
           echo "The file exists."
           break  # Exit the loop since a valid path was entered
   	else
       	   echo "The file does not exist or the path is incorrect."
    	fi
      done  
      break
   elif [[ "$dicChoice" == "no" ]]; then  	#If the file does not exist (user choose no) 
       touch dictionary.txt	 #Create the file
       dicFile="dictionary.txt"
       break
    else  #If the user doesn't enter yes or no keep asking him/her
       	  echo "Please just enter yes or no"
    fi  
done      
while true; do
  clear  # Clear the terminal screen
    # Display the menu options
    echo "Linux Project (Adam Nassan 1202076  Laith Abdalrazzaq 1190715)"
    echo "c.  compress, or compression means compression"
    echo "d.  decompress, decompression means decompression"
    echo "e.  Exit"
    # Read user's choice
    read -p "Enter your choice: " choice
    
    # Handle the user's choice
    case $choice in
        c)
            echo "You chose Compression."
            	#The second time we try to add words(Flag)
                dicFlag=$((dicFlag + 1))
		# Specify input filename
		cat /dev/null > temp.txt 	#empty temp file
		cat /dev/null > compressedfile.txt 	#empty decompressedfile
		read -p "Enter the path of the file you want to compress: " input_filename 
		# Check if the input file exists
		if [ -f "$input_filename" ]; then
		    # Read the file character by character
		    word=""
		    while IFS= read -r -n1 char; do 
		    specialword=$word 	#store the varibale word in the varibale specialword
		    word="$word$char" 	#keep storing characters in variable word until some conditions         
		    hex_value=$(printf '%x' "'$char")
		    if [[ "$char" =~ [[:punct:]] ]]; then 	#if we reached special character
			echo "$specialword" >> temp.txt	  #store the word before we the speical character in temp file 
			echo "$char" >> temp.txt	  #store the special character in the line after
			word=""  
		    elif [[ "$char" == " " ]]; then	#if we reached space
			echo "$specialword" >> temp.txt 	 #store the word before we the space in temp file 
			echo "Space" >> temp.txt	#store the space in the line after
			word="" 
		    elif [[ $hex_value == "0" ]]; then		#if we reached newline 
			echo "$specialword" >> temp.txt   	#store the word before we the newline in temp file 
			echo "\n" >> temp.txt 		#store the newline in the line after
			word=""       
		    fi    
		    done < "$input_filename"        
		    sed -i '$d' temp.txt 	 #delete last line from the temp file
		    sed -i '/^$/d' temp.txt 	#delete empty lines from the temp file

		#read the temp file line by line
		while IFS= read -r line; do 
		     #check if the dicitonary file is empty
		      if [ ! -s "$dicFile" ]; then
		      EmptyFlag="Empty"   #declare a flag empty with value (Empty)
		      echo "01235846avs" >> "$dicFile"
		      fi
		     #read the dictionary file line by line	
		      while IFS= read -r lines; do
		      word=$(echo "$lines" | cut -d ' ' -f2) 	#reach only to the words part in the dictionary to compare
		      word=$(echo "$word" | sed 's/^[[:space:]]*//') 	#delete the spaces before the word to compare correctly
			if [[ "$line" == "$word" ]]; then	 #now compare the word in the temp file to each word in the dictionary
			   flag="repeated"   #If we found the word then declare flag with value (repated)
			   break
			fi          
		      done < dictionary.txt
		      if [[ $flag == "repeated" ]]; then # depending on the flag above if the word in the dictionary then do nothing
			flag="not"
			 continue
		      else	# else if the word is not in the dictionary
		          if [ "$dicFlag" -eq 2 ]; then
			  HexCode=$(wc -l < "$dicFile")      #define varibale hexCode that equals the number of line we reached in the dictionary
			  HexCode=$(printf "0x%.4X" "$HexCode") #convert the line number from decimal to hexadecimal
			  echo "$HexCode 	$line" >> "$dicFile" #finally add the word and its code in the dictionary
			  else
			  #Same as above but the difference we want to avoid special case in the second time we try to add word
			  HexCode=$(wc -l < "$dicFile")
			  HexCode=$(($HexCode - 1))
			  HexCode=$(printf "0x%.4X" "$HexCode")
			  echo "$HexCode 	$line" >> "$dicFile"
			  fi
		      fi
		  done < temp.txt
			if [[ $EmptyFlag == "Empty" ]]; then #check if the dictionary file was initially empty
		  	sed -i '1d' "$dicFile" #delete the first line of the dictionary file
		  	EmptyFlag="Full" #get the flag value back to full
		  	fi
		        echo "Dictionary file filled succesfully"
		    # Read the temp file line by line
		 while IFS= read -r line; do	
		    # Read the dictionary file line by line	 
		   while IFS= read -r lines; do
		    word=$(echo "$lines" | cut -d ' ' -f2) #split using spaces and get second field
		      word=$(echo "$word" | sed 's/^[[:space:]]*//') #Remove leading white spaces in the line
			if [[ "$line" == "$word" ]]; then  #if the word in temp found in dictionary 
			   hex_part="${lines%% *}" #clear after the space (get only the appropiate hex part in the dictionary)
		  	   echo "$hex_part" >> compressedfile.txt #finally add the hex part of each word we found in the dictionary
			   break
			   fi
		   done < "$dicFile"
		 done < temp.txt
		 echo "The file compressed succesfully"
		 
		 charCount=$(wc -m < "$input_filename")   #count number of characters in the uncompressed file
		 charCount=$((charCount - 1))    	   #-1 for last space character added to the file
		 UncompressedSize=$((charCount * 16))     #multibly num of characters by 16 (unicode size)
		 UncompressedSizeBytes=$((UncompressedSize / 8))    #div by 8 to convert bits --> bytes
		 echo "The uncompressed file size = Number of characters’ x 16 (size of the Unicode)"
		 echo "		$charCount x 16 = $UncompressedSize bits = $UncompressedSizeBytes bytes"	
		 
		 numOfLines=$(wc -l < compressedfile.txt) #count number of line in the compressed file
		 CompressedSize=$((numOfLines * 16))       # multibly by 16 (code size)
		 CompressedSizeBytes=$((CompressedSize / 8)) #div by 8 to convert bits --> bytes
		 echo "The compressed file size = Number of codes x 16 (code size)"
		 echo "			 = $numOfLines x 16 = $CompressedSize bits = $CompressedSizeBytes bytes"
		 
		 #div uncompressed by compressed to get the ratio / bc handle floating-point operations / scale 3 precsion by 3
		 CompressionRatio=$(echo "scale=3; $UncompressedSize / $CompressedSize" | bc) 
		 echo "File Compression Ratio = uncompressed file size / compressed file size"
		 echo "		         = $CompressedSize/$UncompressedSize = $CompressionRatio"
            else
		    echo "Input file not found: $input_filename"
		fi
            
            read -p "Press Enter to continue..."
            ;;
        d)
             echo "You chose decompression."
            cat /dev/null > decompressedfile.txt
            read -p "Enter the path of the file you want to decompress: " inputCompressed
		# Check if the input file exists
		if [ -f "$inputCompressed" ]; then
		  while IFS= read -r line; do 	#read the file we want to decompress line by line
		          breakFlag=" "  #declare break flag
          		  errorFlag=" "  #declare errorflag
		   while IFS= read -r lines; do	   #read the dictionary file line by line
		        hex_part="${lines%% *}" #clear after the space to only reach the hex part
			if [[ "$line" == "$hex_part" ]]; then    # if the word found in the dictioanry then give errorflag no errors
			   errorFlag="no erorrs"        
			   word=$(echo "$lines" | cut -d ' ' -f2) # split using spaces and get second field only word field
		           word=$(echo "$word" | sed 's/^[[:space:]]*//') #Remove leading white spaces in the line
		           if [[ $word == "Space" ]]; then   #If the hex part mathced space 
		              echo -n " " >> decompressedfile.txt    # then print " " in the decompressedfile
		           elif [[ $word == '\n' ]]; then     #If the hex part matched \n
		              echo "" >> decompressedfile.txt     # print new line in the decompressedfile
		           else   
		  	   echo -n "$word" >> decompressedfile.txt  #else print the matched word in the decompressedfile
 			   fi
			   break
		        fi
		   done < "$dicFile"
		  if [[ "$errorFlag" == "no erorrs" ]]; then    #depending on errorflag if no errors then do nothing
		   	continue
		  else
		   breakFlag="break"   #else give break flag value of break
		   break		#then break the loop
		  fi
		 done < "$inputCompressed"	 
		   if [[ "$breakFlag" == "break" ]]; then   #if breakflag point to break 
		       echo ""				    # then print error message	
		       echo "The word: $line is not in the dictionary"
		       echo "Failed to decompress"
		       echo ""
		   else    				  # then print the operation done succesfully	
		      echo ""
		      echo "The file decompressed succesfully"
		      echo ""
		   fi
                else
		    echo "Input file not found: $inputCompressed"
		fi
            read -p "Press Enter to continue..."
            ;;
        e)
            echo "Exiting..."
            exit 1		#if the choice is e then end the program 
            ;;
        *)
            echo "Invalid choice. Please select a valid option."  # if the choice doesn't matched then keep asking for other choice
            read -p "Press Enter to continue..."
            ;;
    esac
done 
