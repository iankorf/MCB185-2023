echo "scale=812; 4*a(1)" | bc -l | tail -1 | awk '{print substr($1, 60, 6)}' | echo $(xxd -r -p)
