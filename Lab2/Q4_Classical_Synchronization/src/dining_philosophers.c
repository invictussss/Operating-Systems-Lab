#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define N 5

sem_t forks[N];
pthread_t philosophers[N];

void* philosopher(void* arg)
{
    int id = *(int*)arg;

    int left = id;
    int right = (id + 1) % N;

    printf("Philosopher %d is thinking.\n", id + 1);
    sleep(1);

    sem_wait(&forks[left]);
    printf("Philosopher %d picked up left fork.\n", id + 1);

    sem_wait(&forks[right]);
    printf("Philosopher %d picked up right fork.\n", id + 1);

    printf("Philosopher %d is eating.\n", id + 1);
    sleep(1);

    sem_post(&forks[right]);
    sem_post(&forks[left]);

    printf("Philosopher %d finished eating and put down forks.\n", id + 1);

    return NULL;
}

int main()
{
    int ids[N];

    printf("DINING PHILOSOPHERS PROBLEM\n\n");

    for (int i = 0; i < N; i++)
    {
        sem_init(&forks[i], 0, 1);
    }

    for (int i = 0; i < N; i++)
    {
        ids[i] = i;
        pthread_create(&philosophers[i], NULL, philosopher, &ids[i]);
    }

    for (int i = 0; i < N; i++)
    {
        pthread_join(philosophers[i], NULL);
    }

    for (int i = 0; i < N; i++)
    {
        sem_destroy(&forks[i]);
    }

    printf("\nDining Philosophers execution completed.\n");

    return 0;
}
