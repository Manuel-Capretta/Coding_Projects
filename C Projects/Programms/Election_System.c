#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

void election();
void Voter_define();

//Voter Entity Structure
struct Voter {
  int vote;
  char name[20];
};





int main() {
  int Votes = 0;
  int side_a = 0;
  int side_b = 0;

  //The Voiters names
  char Input_name0[20];
  char Input_name1[20];
  char Input_name2[20];
  char Input_name3[20];
  char Input_name4[20];
  char Input_name5[20];
  char Input_name6[20];
  char Input_name7[20];
  char Input_name8[20];
  char Input_name9[20];

  //Create a Voter Array to store the voters in a single Variable
  struct Voter Voter_arr[10];

  /*****************************************************************************************************/
  //Get the Voters Names
  printf("Voter 1 your name please: ");
  fgets(Input_name0, 20, stdin);
  printf("Voter 2 your name please: ");
  fgets(Input_name1, 20, stdin);
  printf("Voter 3 your name please: ");
  fgets(Input_name2, 20, stdin);
  printf("Voter 4 your name please: ");
  fgets(Input_name3, 20, stdin);
  printf("Voter 5 your name please: ");
  fgets(Input_name4, 20, stdin);
  printf("Voter 6 your name please: ");
  fgets(Input_name5, 20, stdin);
  printf("Voter 7 your name please: ");
  fgets(Input_name6, 20, stdin);
  printf("Voter 8 your name please: ");
  fgets(Input_name7, 20, stdin);
  printf("Voter 9 your name please: ");
  fgets(Input_name8, 20, stdin);
  printf("Voter 10 your name please: ");
  fgets(Input_name9, 20, stdin);

  //Voters
  struct Voter Voter_obj0;
  Voter_obj0.vote;
  strncpy(Voter_obj0.name, Input_name0, 20);

  struct Voter Voter_obj1;
  Voter_obj1.vote;
  strncpy(Voter_obj1.name, Input_name1, 20);

  struct Voter Voter_obj2;
  Voter_obj2.vote;
  strncpy(Voter_obj2.name, Input_name2, 20);

  struct Voter Voter_obj3;
  Voter_obj3.vote;
  strncpy(Voter_obj3.name, Input_name3, 20);

  struct Voter Voter_obj4;
  Voter_obj4.vote;
  strncpy(Voter_obj4.name, Input_name4, 20);

  struct Voter Voter_obj5;
  Voter_obj5.vote;
  strncpy(Voter_obj5.name, Input_name5, 20);

  struct Voter Voter_obj6;
  Voter_obj6.vote;
  strncpy(Voter_obj6.name, Input_name6, 20);

  struct Voter Voter_obj7;
  Voter_obj7.vote;
  strncpy(Voter_obj7.name, Input_name7, 20);

  struct Voter Voter_obj8;
  Voter_obj8.vote;
  strncpy(Voter_obj8.name, Input_name8, 20);

  struct Voter Voter_obj9;
  Voter_obj9.vote;
  strncpy(Voter_obj9.name, Input_name9, 20);

  //Assign Voters to their place in the Voter Array
  Voter_arr[0] = Voter_obj0;
  Voter_arr[1] = Voter_obj1;
  Voter_arr[2] = Voter_obj2;
  Voter_arr[3] = Voter_obj3;
  Voter_arr[4] = Voter_obj4;
  Voter_arr[5] = Voter_obj5;
  Voter_arr[6] = Voter_obj6;
  Voter_arr[7] = Voter_obj7;
  Voter_arr[8] = Voter_obj8;
  Voter_arr[9] = Voter_obj9;

  //print the name of the voters
  //printf("These are the Voters names: \n");
  /*for(int i = 0; i < 11; i++){
    printf("%s", Voter_arr[i]);
  }*/
/*****************************************************************************************************/
 
  printf("This is an Election System. It works very simple. Here are the Rules: \n - Press the 'A' Key to Vote for Side A \n - Press the 'B' Key to Vote for Side B \n - Any other Key pressed during the election time won't count as a vote\n First off, let's get the Vorters Names.\n"); 
  printf("Voting's up. Vote with 1 (for Side A) and 2 (for Side B). \n Let The Voting Beginn. Input the votes now: ");

  election(Votes, side_a, side_b);
}





void election(Votes, side_a, side_b){
  int vote_a = 0, vote_b = 0, Input_vote;
  int voting_done = false;

  /*int* point = 1; //pointer-to-object value 
  printf("%s", Voter_arr[point]); //print out the voters names*/

  //Check for the Vote given by the Voter 
  scanf("%d", & Input_vote);
  if (Votes < 10) {
    if (Input_vote == 1) {
      Input_vote = 0;
      side_a++;
      Votes++;
      printf("\n Side A: %d | Side B: %d\n\n", side_a, side_b);
      printf("Voted for Side A. %d Votes done. Next Vote: ", Votes);
    } else if (Input_vote == 2) {
      Input_vote = 0;
      side_b++;
      Votes++;
      printf("\n Side A: %d | Side B: %d\n\n", side_a, side_b);
      printf("Voted for Side B. %d Votes done. Next Vote: ", Votes);
    } else {
      Input_vote = 0;
      Votes++;
      printf("\n Side A: %d | Side B: %d\n\n", side_a, side_b);
      printf("Invalid Vote.     %d Votes done. Next Vote: ", Votes);
    }
  }

  //Check weather or not the Voting time has exceeded and perform a recursive algorythm if it didn't
  if (Votes < 10) {
    election(Votes, side_a, side_b);
  } else {
    printf("\nVoting's up. Time for the results:");
    printf("\n Side A: %d / Side B: %d", side_a, side_b);
    if(side_a > side_b){
      printf("\nSide A won the election");
      voting_done = true;
    } else if(side_a < side_b){
      printf("\nSide B won the election");
      voting_done = true;
    } else {
      printf("\nIt's a Draw. Noone won the election");
      voting_done = true;
    }
  }

  if(voting_done){
    for(int i = 0; i < 10; i++){
    }
  }
}