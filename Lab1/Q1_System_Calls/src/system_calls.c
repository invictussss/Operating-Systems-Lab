#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <string.h>

void file_operation()
{
    int fd;
    char buffer[100];

    fd = open("child_record.txt", O_CREAT | O_WRONLY | O_TRUNC, 0644);

    if (fd == -1)
    {
        perror("File creation failed");
        return;
    }

    char message[] = "File created by the child process.\n";

    write(fd, message, strlen(message));
    close(fd);

    fd = open("child_record.txt", O_RDONLY);

    if (fd == -1)
    {
        perror("File opening failed");
        return;
    }

    int bytes = read(fd, buffer, sizeof(buffer) - 1);
    buffer[bytes] = '\0';

    printf("File content: %s", buffer);

    close(fd);
}

int main()
{
    pid_t child;
    int status;

    printf("Parent PID: %d\n", getpid());

    child = fork();

    if (child < 0)
    {
        perror("Fork failed");
        return 1;
    }

    if (child == 0)
    {
        printf("\nChild PID: %d\n", getpid());
        printf("Child's Parent PID: %d\n", getppid());

        file_operation();

        printf("\nRunning ls command using exec...\n");

        execlp("ls", "ls", "-lh", (char *)NULL);

        perror("exec failed");
        _exit(1);
    }
    else
    {
        printf("Parent is waiting for child...\n");

        waitpid(child, &status, 0);

        if (WIFEXITED(status))
        {
            printf("\nChild exited with status: %d\n",
                   WEXITSTATUS(status));
        }
    }

    return 0;
}
