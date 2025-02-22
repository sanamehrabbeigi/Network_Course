from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
        Host3 = self.addHost( 'h3' )
        Host4 = self.addHost( 'h4' )
        Host5 = self.addHost( 'h5' )
        Host6 = self.addHost( 'h6' )
        Host7 = self.addHost( 'h7' )
        Host8 = self.addHost( 'h8' )
        Host9 = self.addHost( 'h9' )
        Host10 = self.addHost( 'h10' )

        Switch1 = self.addSwitch( 's11' )
        Switch2 = self.addSwitch( 's12' )
        Switch3 = self.addSwitch( 's13' )
        Switch4 = self.addSwitch( 's14' )
        Switch5 = self.addSwitch( 's15' )
        Switch6 = self.addSwitch( 's16' )
        Switch7 = self.addSwitch( 's17' )
        Switch8 = self.addSwitch( 's18' )
        Switch9 = self.addSwitch( 's19' )
        Switch10 = self.addSwitch( 's20' )

    # Add links
    self.addLink( Host1, Switch1)
	self.addLink( Switch1, Switch2)
	self.addLink( Switch2, Host2)
	
	self.addLink( Host3, Switch3 )
	self.addLink( Switch3, Switch4 )
	self.addLink( Switch4, Host4 )

	self.addLink( Host5, Switch5 )
	self.addLink( Switch5, Switch6 )
	self.addLink( Switch6, Host6 )

	self.addLink( Host7, Switch7 )
	self.addLink( Switch7, Switch8 )
	self.addLink( Switch8, Host8 )

	self.addLink( Host9, Switch9 )
	self.addLink( Switch9, Switch10 )
	self.addLink( Switch10, Host10 )
	
	self.addLink( Switch1, Switch3 )
	self.addLink( Switch3, Switch5 )
	self.addLink( Switch5, Switch7 )
	self.addLink( Switch7, Switch9 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
