<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import Input from './Input.svelte';

  let isPopupOpen = false;
  const dispatch = createEventDispatcher();

  function openPopup() {
    isPopupOpen = true;
  }

  function closePopup() {
    isPopupOpen = false;
  }
</script>

<div class="container h-full mx-auto flex justify-center items-center">
  <div class="flex flex-col">
    <button on:click={openPopup}>Add Book</button>
    {#if isPopupOpen}
      <div class="overlay" style="z-index: 999;">
        <div class="popup">
            <form action="/?/addbook" method="POST">
                <Input class="block text-sm font-medium text-gray-700" id="name" label="Name" type="text" />
                <Input class="block text-sm font-medium text-gray-700" id="description" label="Description" type="textarea" cols="30" rows="5"/>
                <Input class="block text-sm font-medium text-gray-700" id="author" label="Author" type="text" />
                <Input class="block text-sm font-medium text-gray-700" id="genre" label="Genre" type="text" />
                <Input class="block text-sm font-medium text-gray-700" id="rating" label="Rating" type="number" min="1" max="10" />
                <button type="submit" class="mt-4 w-full px-4 py-2 bg-indigo-600 text-white font-semibold rounded-md focus:outline-none focus:shadow-outline-indigo">Add Book</button>
                <button class="close-button ml-auto" on:click={closePopup}>x</button>
          </form>
        </div>
      </div>
    {/if}
  </div>
</div>

<style>
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .popup {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
  }

  .close-button {
    background-color: transparent;
    border: none;
    cursor: pointer;
  }
</style>
