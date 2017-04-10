from JumpScale import j

class Actions():
    def init(self):
        # nothing to do
        pass

    def install(self):
        """
        Deploy and run a drupal website
        """
        if 'dockercompose' not in self.service.producers:
            raise j.exceptions.AYSNotFound('The dockercompose service is not found')
        
        # reading ip from the dockercompose service
        dcompose = self.service.getProducers('dockercompose')[0]
        
        host = dcompose.hrd.get('ssh')
        c = j.tools.cuisine.get(j.tools.executor.getSSHBased(addr=host))
        
        drusite = 'https://ftp.drupal.org/files/projects'
        drufile = 'drupal-8.1.0.tar.gz'
        tmppath = '/tmp'
        
        composer = 'https://github.com/RobLoach/docker-compose-drupal'
        destination = '/opt/drupal-compose'
        
        # download drupal if not already done
        if not c.core.file_exists('%s/%s' % (tmppath, drufile)):
            c.core.run('wget %s/%s -O %s/%s' % (drusite, drufile, tmppath, drufile))
        
        # cloning composer repository
        # c.git.pullRepo(composer, destination)
        if not c.core.dir_exists(destination):
            c.core.run('git clone %s %s' % (composer, destination))
        
        # extracting drupal to composer directory
        if not c.core.dir_exists('%s/drupal' % destination):
            c.core.run('tar -xf %s/%s -C %s' % (tmppath, drufile, destination))
            c.core.run('mv %s/drupal-* %s/drupal' % (destination, destination))
        
        c.docker.compose.up(destination, True)
