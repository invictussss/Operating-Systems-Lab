#include <stdio.h>
#include <pthread.h>

#define THREADS 2
#define INCREMENTS 1000000

long long counter = 0;
long long mutex_counter = 0;

pthread_mutex_t lock;

void* unsafe_increment(void* arg)
{
    for (int i = 0; i < INCREMENTS; i++)
    {
        counter++;
    }

    return NULL;
}

void* safe_increment(void* arg)
{
    for (int i = 0; i < INCREMENTS; i++)
    {
        pthread_mutex_lock(&lock);

        mutex_counter++;

        pthread_mutex_unlock(&lock);
    }

    return NULL;
}

int main()
{
    pthread_t threads[THREADS];

    pthread_mutex_init(&lock, NULL);

    printf("RACE CONDITION USING MUTEX\n");
    printf("Threads: %d\n", THREADS);
    printf("Increments per thread: %d\n", INCREMENTS);

    // Unsafe execution
    for (int i = 0; i < THREADS; i++)
    {
        pthread_create(&threads[i], NULL, unsafe_increment, NULL);
    }

    for (int i = 0; i < THREADS; i++)
    {
        pthread_join(threads[i], NULL);
    }

    printf("\n--- Without Mutex ---\n");
    printf("Expected Counter: %d\n", THREADS * INCREMENTS);
    printf("Actual Counter: %lld\n", counter);

    // Safe execution
    for (int i = 0; i < THREADS; i++)
    {
        pthread_create(&threads[i], NULL, safe_increment, NULL);
    }

    for (int i = 0; i < THREADS; i++)
    {
        pthread_join(threads[i], NULL);
    }

    printf("\n--- With Mutex ---\n");
    printf("Expected Counter: %d\n", THREADS * INCREMENTS);
    printf("Actual Counter: %lld\n", mutex_counter);

    pthread_mutex_destroy(&lock);

    return 0;
}
