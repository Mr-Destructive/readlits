<script lang="ts">
import { Client, Databases } from 'appwrite';
import Book from './Book.svelte';
let books: Book[] = [];

const client = new Client()
  .setEndpoint('http://127.0.0.1:8001/v1')
  .setProject('6467a226111048c72b2c');
  const databases = new Databases(client);

  try {
    const promise = databases.listDocuments(
      '6467a2917aaf8fd17198',
      '6467a33ecbefa946e984',
    );
    promise.then(function (response) {
        books = response.documents;
    }, function (error) {
        console.log(error);
    });
  } catch (error) {
    console.error(error);
  }

</script>

<h2 class="text-3xl font-bold mb-8">Book List</h2> 

<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
  {#if books}
    {#each books as book}
      <div class="flex flex-col rounded-lg hover:shadow-lg transform transition duration-500 hover:scale-105">
      <a href="/books/{book.$id}">
        <div class="relative">
          <img class="w-full h-64 object-cover rounded-t-lg" src={book.cover_image ? book.cover_image : 'https://placehold.it/150x150'} alt={book.name} />
          <div class="absolute right-0 top-0 px-2 py-1 bg-gray-800 rounded-bl-lg text-white">
            <span class="text-sm">{book.rating}</span>
            <svg viewBox="0 0 20 20" fill="currentColor" class="star w-4 h-4 inline-block">
              <path
                fill-rule="evenodd"
                d="M10 1.583l2.65 5.369 5.904.858-4.275 4.175.99 5.778L10 15.525l-5.269 2.84.99-5.778-4.275-4.175 5.904-.858L10 1.583z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </div>
        </div>
        <div class="p-4 border border-t-0 rounded-b-lg flex-1 flex flex-col">
          <h3 class="text-xl font-bold mb-2">{book.name}</h3>
          <p class="text-gray-700 mb-3">{book.Author}</p>
          <p class="text-gray-600 text-sm flex-1">{book.description}</p>
        </div>
        </a>
      </div>
    {/each}
  {/if}
</div>
