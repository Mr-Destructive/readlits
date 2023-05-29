
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
    <textarea id={id} {...$$restProps}></textarea>
  {:else if type === 'number'}
    <input type="number" id={id} {...$$restProps} />
  {:else}
    <input type="text" id={id} {...$$restProps} />
  {/if}
</label>

<style>
  label {
    flex: 1;
  }
</style>

