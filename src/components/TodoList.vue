<template>
  <div>
    <ul>
      <TodoItem v-for="(todo, i) in todos"
      v-bind:todo="todo"
      v-bind:key="todo"
      v-bind:index="i"
      v-on:remove-todo="removeTodo"

      />
    </ul>
  </div>
</template>
<script>
import TodoItem from '@/components/TodoItem'
export default {
  props: ['todos'],
  components: {TodoItem},
  methods:{
    removeTodo(id){
      this.$emit('remove-todo', id)
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
