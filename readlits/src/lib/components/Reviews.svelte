<script lang="ts">
  import { onMount } from 'svelte';

  import { Client, Databases } from 'appwrite';
  import Review from './Review.svelte';

  let reviews: Review[] = [];

  const client = new Client()
    .setEndpoint('http://127.0.0.1:8001/v1')
    .setProject('6467a226111048c72b2c');
  const databases = new Databases(client);
  let promise;
const formatDate = (dateStr) => {
  const date = new Date(dateStr);
  const day = date.getDate();
  const month = new Intl.DateTimeFormat('en-US', { month: 'short' }).format(date);
  const year = date.getFullYear();

  return `${day} ${month} ${year}`;
};

  onMount(() => {
    try {
      promise = databases.listDocuments('6467a2917aaf8fd17198', '6472219e144e1f6135ea');
      promise
        .then(function (response) {
          reviews = response.documents;
          console.log(reviews)
        })
        .catch(function (error) {
          console.log(error);
        });
    } catch (error) {
      console.error(error);
    }
  });
  console.log(reviews)
</script>
{#await promise}
  <p>Loading reviews...</p> 
{/await}

<div class="grid grid-cols-1 gap-4">
  {#if reviews.length > 0}
    {#each reviews as review}
      <div class="review-card p-4">
        <p class="review-text">{review.review}</p>
        <p class="review-user">{review.user ? review.user : 'Anonymous'}</p>
        <p class="review-date">Reviewd at: {formatDate(review.$createdAt)}</p>
      </div>
    {/each}
  {/if}
</div>

<style>
  .review-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 1rem;
    margin: 1rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease-in-out;
  }

  .review-card:hover {
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
    transform: scale(1.03);
  }

  .review-text {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: #333;
  }

  .review-user {
    font-size: 1rem;
    font-style: italic;
    color: #666;
  }
</style>
