nextflow.enable.dsl=2

include { gptPromptForText } from 'plugin/nf-gpt'

workflow {

    // define input
    def query = Channel
                .fromPath( 'data/data.bf' )
                .map { it -> it.text }

    query.view()

    // parse input to gpt prompt
    println gptPromptForText(query)
}