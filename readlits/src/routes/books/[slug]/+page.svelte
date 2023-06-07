<script lang="ts">
    import Reviews from '$lib/components/Reviews.svelte';
    import type { PageData } from './$types';
    export let data: PageData;
</script>

<a href='/books'>Books</a>
<h1 class="text-4xl font-bold mb-4">{data.title}</h1>
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
  <div class="aspect-w-2 aspect-h-3">
    <img class="object-cover rounded-lg shadow-lg" src={data.cover_image} alt={data.title} />
  </div>
  <div class="flex flex-col">
    <h2 class="text-2xl font-semibold mb-2">{data.author}</h2>
    <p class="text-gray-600 mb-4">{data.content}</p>
    <h3 class="text-lg font-semibold mb-2">Genre: {data.genre}</h3>
    <div class="mb-4">
      <h4 class="text-md font-semibold mb-2">Rating:</h4>
      <div class="flex items-center">
        <svg viewBox="0 0 20 20" fill="currentColor" class="star w-5 h-5 text-yellow-400">
          <path
            fill-rule="evenodd"
            d="M10 1.583l2.65 5.369 5.904.858-4.275 4.175.99 5.778L10 15.525l-5.269 2.84.99-5.778-4.275-4.175 5.904-.858L10 1.583z"
            clip-rule="evenodd"
          ></path>
        </svg>
        <p class="text-lg font-semibold ml-2">{data.rating}</p>
      </div>
    </div>
    <div>
      <h4 class="text-md font-semibold mb-2">Reviews:</h4>
        <ul class="list-disc">
        <Reviews/>
        </ul>
    </div>
  </div>
</div>


<h1>{data.title}</h1>
<div>{@html data.content}</div>
