#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

sem_t wrt;
pthread_mutex_t mutex;

int read_count = 0;
int shared_data = 100;

void* reader(void* arg)
{
    int id = *(int*)arg;

    pthread_mutex_lock(&mutex);

    read_count++;

    if (read_count == 1)
    {
        sem_wait(&wrt);
    }

    pthread_mutex_unlock(&mutex);

    printf("Reader %d is reading data: %d\n", id, shared_data);
    sleep(1);

    pthread_mutex_lock(&mutex);

    read_count--;

    if (read_count == 0)
    {
        sem_post(&wrt);
    }

    pthread_mutex_unlock(&mutex);

    printf("Reader %d finished reading.\n", id);

    return NULL;
}

void* writer(void* arg)
{
    int id = *(int*)arg;

    sem_wait(&wrt);

    shared_data += 10;

    printf("Writer %d is writing data: %d\n", id, shared_data);
    sleep(1);

    printf("Writer %d finished writing.\n", id);

    sem_post(&wrt);

    return NULL;
}

int main()
{
    pthread_t readers[3], writers[2];

    int reader_ids[3] = {1, 2, 3};
    int writer_ids[2] = {1, 2};

    sem_init(&wrt, 0, 1);
    pthread_mutex_init(&mutex, NULL);

    printf("READERS-WRITERS PROBLEM\n\n");

    for (int i = 0; i < 3; i++)
    {
        pthread_create(&readers[i], NULL, reader, &reader_ids[i]);
    }

    for (int i = 0; i < 2; i++)
    {
        pthread_create(&writers[i], NULL, writer, &writer_ids[i]);
    }

    for (int i = 0; i < 3; i++)
    {
        pthread_join(readers[i], NULL);
    }

    for (int i = 0; i < 2; i++)
    {
        pthread_join(writers[i], NULL);
    }

    sem_destroy(&wrt);
    pthread_mutex_destroy(&mutex);

    printf("\nReaders-Writers execution completed.\n");
    printf("Final Shared Data: %d\n", shared_data);

    return 0;
}
