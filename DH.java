import java.util.*;
 
class Diffie_Hellman
{
 public static void main(String args[])
 {
 int p=23;
 int g=9;
 int a=3;
 int b=4;
 
 int A = (int)Math.pow(g,a)%p;
 int B = (int)Math.pow(g,b)%p;
 
 int S_A = (int)Math.pow(B,a)%p;
 int S_B =(int)Math.pow(A,b)%p; 
    
 } 
}