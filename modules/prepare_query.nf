process write_to_file {

    input:
    file input_path
    path output_path
    val question

    output:
    path "${output_path}/query.txt", emit: query

    script:
    """
    python3 "$projectDir/bin/parseData.py" -i "${input_path}" -o "${output_path}/query.txt" -q "${question}"
    """
}