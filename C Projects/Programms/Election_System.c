#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

void election();
void Voter_define();
int done();

//Voter Entity Structure
struct Voter {
  char name[20];
};





int main() {
  int Votes = 0;
	int maxVotes = 10;
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
  strncpy(Voter_obj0.name, Input_name0, 20);

  struct Voter Voter_obj1;
  strncpy(Voter_obj1.name, Input_name1, 20);

  struct Voter Voter_obj2;
  strncpy(Voter_obj2.name, Input_name2, 20);

  struct Voter Voter_obj3;
  strncpy(Voter_obj3.name, Input_name3, 20);

  struct Voter Voter_obj4;
  strncpy(Voter_obj4.name, Input_name4, 20);

  struct Voter Voter_obj5;
  strncpy(Voter_obj5.name, Input_name5, 20);

  struct Voter Voter_obj6;
  strncpy(Voter_obj6.name, Input_name6, 20);

  struct Voter Voter_obj7;
  strncpy(Voter_obj7.name, Input_name7, 20);

  struct Voter Voter_obj8;
  strncpy(Voter_obj8.name, Input_name8, 20);

  struct Voter Voter_obj9;
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
  printf("These are the Voters names: \n");
  for(int i = 0; i <= 10; i++){
    printf("%d: %s", i, Voter_arr[i].name);
  }
/*****************************************************************************************************/
 
  printf("This is an Election System. It works very simple. Here are the Rules: \n - Press the 'A' Key to Vote for Side A \n - Press the 'B' Key to Vote for Side B \n - Any other Key pressed during the election time won't count as a vote\n First off, let's get the Vorters Names.\n"); 
  printf("Voting's up. Vote with 1 (for Side A) and 2 (for Side B). \n Let The Voting Beginn. Input the votes now: ");

  election(Votes, maxVotes, side_a, side_b);
}





void election(Votes, maxVotes, side_a, side_b){
  int vote_a = 0, vote_b = 0, Input_vote;

  //Check for the Vote given by the Voter 
  scanf("%d", & Input_vote);
  if (Votes < maxVotes) {
    if(Input_vote == 1){
      side_a++;
      Votes++;
      printf("\n Side A: %d | Side B: %d\n\n", side_a, side_b);
      printf("Voted for Side A. %d Votes done. Next Vote: ", Votes);
      done(Votes, maxVotes, side_a, side_b);
    } else if(Input_vote == 2){
      side_b++;
      Votes++;
      printf("\n Side A: %d | Side B: %d\n\n", side_a, side_b);
      printf("Voted for Side B. %d Votes done. Next Vote: ", Votes);
      done(Votes, maxVotes, side_a, side_b);
    } else {
      Votes++;
      printf("\n Side A: %d | Side B: %d\n\n", side_a, side_b);
      printf("Invalid Vote.     %d Votes done. Next Vote: ", Votes);
      done(Votes, maxVotes, side_a, side_b);
    }
  }
}



int done(Votes, maxVotes, side_a, side_b){
  int voting_done = false;

  //Check weather or not the Voting time has exceeded and perform a recursive algorythm if it didn't
  if (Votes < maxVotes) {
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

  return Votes, maxVotes, side_a, side_b;
}