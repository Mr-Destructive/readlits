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
  let selectedBook = books[0];

</script>

<h2 class="text-xl font-semibold mb-4">Book List</h2> 
<ul id="books" class="list-disc flex flex-wrap -mx-4">
{#if books}
{#each books as book}
  <li class="mb-4 px-11 flex-1/2 h-full">
    <a href="#/book" on:click={() => selectedBook = book}>
      <img class="w-16 h-16 rounded-full object-cover" src="https://placehold.it/150x150" alt="Book cover">
      <div class="h-full flex flex-col justify-between">
        <h5 class="text-base font-semibold mb-2">{book.name}</h5>
        <div class="text-sm text-gray-500">{book.rating}</div>
      </div>
    </a>
    {#if selectedBook === book }
      <Book />
    {/if}
  </li> 
{/each}
{/if}
</ul>
