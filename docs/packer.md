# To build new packer image

1. Update version in ami-name in `packer/resero-labs-dl.packer`
2. Run the following: 
    ```bash
    $ cd packer
    $ packer build resero-labs-dl.packer
    ```
3. after testing, use the AWS console to change the image currently named "resero-labs-dlami" to
"resero-labs-dlami-<dated.version>", and change the name of the image just created, 
"resero-labs-dlami-latest" to "resero-labs-dlami"

**Note**: the `b` in the AMI name indicates the AWS Deep Learning AMI Version number that was used
as a base for the AMI 