#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool validate_input(char* command);

int main(){
    char input[4];
    printf("Enter a command:  ");
    scanf("%s",input);
    printf("%s", validate_input(input) ? "True\n" : "False\n");
    return 0;
}

bool validate_input(char* command){
    static int max_command_len = 4;

    int len_command = strlen(command);
    int pos_x = 0;
    int pos_y = 0;
    int orientation = 0;

    //Validate command sequence length is not greater than max
    if(len_command> max_command_len)
    {
        return false;
    }

    //Validate command sequence contains valid actions
    //Validate command sequence to ensure return to origin
    for(int i = 0; i < 4*len_command; i++)
    {
        switch(command[i%len_command])
        {
            case 'L':
                orientation = (orientation + 270) % 360;
                break;
            case 'R':
                orientation = (orientation + 90) % 360;
                break;
            case 'F':
                switch(orientation)
                {
                    case 0:
                        pos_y++;
                        break;
                    case 90:
                        pos_x++;
                        break;
                    case 180:
                        pos_y--;
                        break;
                    case 270:
                        pos_x--;
                        break;
                }
                break;
            default :
                return false;
        }
    }

    if (pos_x == 0 && pos_y == 0){
        return true;
    }

    return false;
}


