
<script lang="ts">
  interface $$Props extends Partial<svelte.JSX.HTMLAttributes<HTMLElementTagNameMap['input']>> {
    id: string;
    label: string;
    type?: 'text' | 'textarea' | 'number'; // Add 'textarea' type
  }
  
  export let id: string;
  export let label: string;
  export let type: 'text' | 'textarea' | 'number' = 'text'; // Set default type to 'text'
</script>

<label for={id} class="mb-2">
  <span>{label}</span>
  {#if type === 'textarea'}
    <textarea id={id} name={id} {...$$restProps}
    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
    ></textarea>
  {:else if type === 'number'}
    <input type="number" id={id} name={id} {...$$restProps} 
    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"/>
  {:else}
    <input type="text" id={id} name={id} {...$$restProps} 
    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"/>
  {/if}
</label>

<style>
  label {
    flex: 1;
  }
</style>

