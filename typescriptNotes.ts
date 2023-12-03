function greet(name: string) {
    console.log(`Hello, ${name}!`);
}

greet("TypeScript");


export function decodedValue(colors: string[]) {
    let abbreviatedColors = colors.splice(0, 2)
    let colorNumArray = []
    for (let i = 0; i < abbreviatedColors.length ; i++) {
      let color = abbreviatedColors[i]
      let colorNum = Colors.indexOf(color)
      colorNumArray.push(colorNum)
    }
    let colorString = colorNumArray.join('')
    let finalNum = Number(colorString)

    return finalNum

  }

  export const Colors: string[]= ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

  console.log(decodedValue(['brown', 'red', 'white']))
