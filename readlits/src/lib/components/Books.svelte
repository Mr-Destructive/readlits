<script lang="ts">
import { Client, Databases, Query } from 'appwrite';

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

<h2 class="text-xl font-semibold mb-4">Book List</h2>
<ul id="books" class="list-disc">
{#if books}
 {#each books as book}
  <li class="mb-4">
    <a href="#/">
      <img class="w-16 h-16 rounded-full object-cover" src="https://placehold.it/150x150" alt="Book cover">
      <h5 class="text-base font-semibold mb-2">{book.name}</h5>
      <div class="text-sm text-gray-500">{book.rating}</div>
    </a>
  </li>
{/each}
{/if}
</ul>
