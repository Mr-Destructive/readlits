<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import Input from './Input.svelte';

  let isPopupOpen = false;
  const dispatch = createEventDispatcher();

  function openPopup() {
    if (isPopupOpen === true){
    isPopupOpen = false;
    } else{
      isPopupOpen = true;
    }
  }
</script>

<div class="container h-full mx-auto flex justify-center items-center">
  <div class="flex flex-col">
    <button on:click={openPopup}>SignUp</button>
    {#if isPopupOpen}
      <div class="overlay" style="z-index: 3;">
        <div class="popup">
            <form action="/?/register" method="POST">
                <Input id="name" label="Name" type="text" />
                <Input id="email" label="Email" type='email' />
                <Input id="password" label="Password" type='password' />
                <button type="submit" class="mt-4 w-full px-4 py-2 bg-indigo-600 text-white font-semibold rounded-md focus:outline-none focus:shadow-outline-indigo">Signup</button>
                <button class="close-button ml-auto" on:click={openPopup}>x</button>
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
