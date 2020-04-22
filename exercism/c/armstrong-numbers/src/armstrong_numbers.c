#include "armstrong_numbers.h"
#include <stdio.h>
#include <math.h>



int is_zero(int input){
  if(input){
    return 0;
  }
  return 1;
}

int get_len(int input){
  len = floor(log10(abs(input))) + 1;
  return len;
}

int * parse_input(int input, int len){
  int i;
  static int number_array[len];
  for(i=0; i<len; i++){
    number_array[i] = input % 10;
    input /= 10;
  }
  return number_array;
}

int is_armstrong_number(int input){
  int i;
  int j;
  int len;
  int total;
  int pow_total;
  int *number_array;

  len = get_len(input);
  
  number_array = parse_input(input, len);

  if(is_zero(input)){
    return 0;  
  }
  
  else{
    pow_total = 1;
    for(i=0;i<len;i++){
      for(j=0;j<len;j++){
       pow_total = number_array[i] * pow_total;
      }
      total += pow_total;
      pow_total = 0;
    }
  
  }
  printf("total: %d", total);
  return total;
}



void main(){
  printf("total: %d", is_armstrong_number(input))    
}



